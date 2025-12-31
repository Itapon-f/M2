/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_calc_moves.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 00:00:00 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 02:34:39 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	exec_moves_both_up(t_stack **from, t_stack **to, int *f, int *t)
{
	while (*f > 0 && *t > 0)
	{
		ft_rr(from, to, 1);
		(*f)--;
		(*t)--;
	}
	while (*f > 0)
	{
		ft_rb(from, 1);
		(*f)--;
	}
	while (*t > 0)
	{
		ft_ra(to, 1);
		(*t)--;
	}
}

static void	exec_moves_both_down(t_stack **from, t_stack **to, int f, int t)
{
	while (f > 0 && t > 0)
	{
		ft_rrr(from, to, 1);
		f--;
		t--;
	}
	while (f > 0)
	{
		ft_rrb(from, 1);
		f--;
	}
	while (t > 0)
	{
		ft_rra(to, 1);
		t--;
	}
}

void	ft_execute_calculated_moves(t_stack **from, t_stack **to,
			t_count_moves *moves)
{
	t_min_max		min_max;
	int				from_size;
	int				to_size;

	if (!moves || !from || !*from)
		return ;
	from_size = ft_stack_size(*from);
	to_size = ft_stack_size(*to);
	moves->from_up = ft_get_position(*from, moves->node);
	moves->to_up = ft_find_target_pos(*to, moves->node->nbr);
	min_max = ft_count_moves_final(moves, to_size, from_size);
	if (min_max.moves_up <= min_max.moves_down
		&& min_max.moves_up <= min_max.moves_up_dwn
		&& min_max.moves_up <= min_max.moves_dwn_up)
		exec_moves_both_up(from, to, &moves->from_up, &moves->to_up);
	else if (min_max.moves_down <= min_max.moves_up_dwn
		&& min_max.moves_down <= min_max.moves_dwn_up)
		exec_moves_both_down(from, to, from_size - moves->from_up,
			to_size - moves->to_up);
	else if (min_max.moves_up_dwn <= min_max.moves_dwn_up)
		ft_ra_rrab(from, to, moves, to_size);
	else
		ft_rra_rb(from, to, moves, from_size);
}
