/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_moves.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 02:34:05 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 02:37:40 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_min_max	ft_count_moves_final(t_count_moves *moves,
			int to_size, int from_size)
{
	t_min_max	min_max;

	if (moves->from_up > moves->to_up)
		min_max.moves_up = moves->from_up;
	else
		min_max.moves_up = moves->to_up;
	if ((from_size - moves->from_up) > (to_size - moves->to_up))
		min_max.moves_down = (from_size - moves->from_up);
	else
		min_max.moves_down = (to_size - moves->to_up);
	min_max.moves_up_dwn = moves->from_up + (to_size - moves->to_up);
	min_max.moves_dwn_up = (from_size - moves->from_up) + moves->to_up;
	return (min_max);
}

int	ft_count_moves(t_count_moves *moves)
{
	t_min_max	min_max;

	if (moves->from_up > moves->to_up)
		min_max.moves_up = moves->from_up;
	else
		min_max.moves_up = moves->to_up;
	if (moves->from_down > moves->to_down)
		min_max.moves_down = moves->from_down;
	else
		min_max.moves_down = moves->to_down;
	min_max.moves_up_dwn = moves->from_up + moves->to_down;
	min_max.moves_dwn_up = moves->from_down + moves->to_up;
	moves->count = min_max.moves_up;
	if (min_max.moves_down < moves->count)
		moves->count = min_max.moves_down;
	if (min_max.moves_up_dwn < moves->count)
		moves->count = min_max.moves_up_dwn;
	if (min_max.moves_dwn_up < moves->count)
		moves->count = min_max.moves_dwn_up;
	return (moves->count);
}

void	ft_stack_total_cost(t_stack **from, t_stack **to,
				t_stack *node, t_count_moves *moves)
{
	int	from_size;
	int	to_size;

	moves->from_up = ft_get_position(*from, node);
	moves->to_up = ft_find_target_pos(*to, node->nbr);
	from_size = ft_stack_size(*from);
	to_size = ft_stack_size(*to);
	moves->node = node;
	moves->from_down = from_size - moves->from_up;
	moves->to_down = to_size - moves->to_up;
	moves->count = ft_count_moves(moves);
}

t_count_moves	*ft_calc_moves(t_stack **from, t_stack **to, int len_from)
{
	t_count_moves	*current_moves;
	t_count_moves	tmp_moves;
	t_stack			*current;
	int				i;

	if (!from || !*from)
		return (NULL);
	current_moves = (t_count_moves *)malloc(sizeof(t_count_moves));
	if (!current_moves)
		return (NULL);
	current = *from;
	ft_stack_total_cost(from, to, current, current_moves);
	i = 1;
	while (i < len_from)
	{
		current = current->next;
		ft_stack_total_cost(from, to, current, &tmp_moves);
		if (tmp_moves.count < current_moves->count)
			*current_moves = tmp_moves;
		i++;
	}
	return (current_moves);
}
